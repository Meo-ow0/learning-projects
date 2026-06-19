import os
import sys
import json
import base64
import cv2
import openai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment. Add it to .env or your environment variables.")

client = openai.OpenAI(api_key=api_key)


def validate_image_path(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return False

    try:
        with Image.open(image_path) as img:
            img.verify()
    except Exception:
        print("Error: The file exists but is not a valid image. Please provide a real JPG/PNG file.")
        return False

    return True


def preprocess_image(image_path):
    if not validate_image_path(image_path):
        return None

    img = cv2.imread(image_path)
    if img is None:
        print("Error: OpenCV could not load the image. Make sure it's a valid JPG/PNG.")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, processed = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite("cleaned_doc.jpg", processed)
    return "cleaned_doc.jpg"


def build_data_url(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


def extract_data(image_path):
    cleaned_path = preprocess_image(image_path)
    if cleaned_path is None:
        return "Failed to process image."
    
    image_url = build_data_url(cleaned_path)

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {"type": "input_text", "text": "Extract the vendor name and total amount from this image. Return strictly valid JSON format."},
                {"type": "input_image", "image_url": image_url},
            ],
            temperature=0.0,
        )
    except Exception as exc:
        return f"OpenAI request failed: {exc}"

    if getattr(response, "output_text", None):
        return response.output_text

    if hasattr(response, "output") and isinstance(response.output, list):
        texts = []
        for item in response.output:
            if isinstance(item, dict) and "content" in item:
                for part in item["content"]:
                    if isinstance(part, dict) and part.get("type") == "output_text" and part.get("text"):
                        texts.append(part["text"])
        if texts:
            return "\n".join(texts)

    return str(response)


def parse_json_output(raw_text):
    if not raw_text:
        return None

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        start = raw_text.find("{")
        end = raw_text.rfind("}")
        if start != -1 and end != -1 and start < end:
            try:
                return json.loads(raw_text[start:end+1])
            except json.JSONDecodeError:
                pass

    return None


def format_extracted_data(parsed):
    if not isinstance(parsed, dict):
        return None

    vendor = parsed.get("vendor") or parsed.get("vendor_name") or parsed.get("supplier")
    total = parsed.get("total") or parsed.get("amount") or parsed.get("total_amount")
    result = []
    if vendor:
        result.append(f"Vendor: {vendor}")
    if total:
        result.append(f"Total amount: {total}")
    return "\n".join(result) if result else None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <image_path>")
        print("Example: python app.py C:\\Users\\Shreya\\Downloads\\download.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    raw_result = extract_data(image_path)
    print("--- Result from AI ---")
    print(raw_result)

    parsed = parse_json_output(raw_result)
    formatted = format_extracted_data(parsed)
    if formatted:
        print("\n--- Parsed Output ---")
        print(formatted)
    elif parsed:
        print("\n--- Parsed JSON ---")
        print(json.dumps(parsed, indent=2))
    else:
        print("\nNote: Could not parse AI output as JSON. Please review raw output above.")
