#include <iostream>
#include <fstream>
#include <vector>

// 1. Structure to hold pixel data
struct Pixel {
    unsigned char b, g, r; // BMP stores colors in Blue-Green-Red order
};

// 2. Core Processing Functions
void applyGrayscale(std::vector<Pixel>& pixels) {
    for (auto& p : pixels) {
        unsigned char avg = (p.r + p.g + p.b) / 3;
        p.r = p.g = p.b = avg;
    }
}

int main() {
    // 3. Simple CLI Menu
    int choice;
    std::cout << "1. Grayscale\n2. Brightness\nChoose an option: ";
    std::cin >> choice;

    // Here you would add logic to:
    // - Open the file
    // - Skip the header (first 54 bytes for BMP)
    // - Read pixels into the vector
    // - Apply function
    // - Save back to new file
    
    return 0;
}