<%@ page import="java.util.Random" %>
<%
    // This is pure Java logic running on the server
    if (session.getAttribute("target") == null) {
        session.setAttribute("target", new Random().nextInt(100) + 1);
        session.setAttribute("attempts", 0);
    }

    String message = "";
    String guessStr = request.getParameter("guess");

    if (guessStr != null) {
        int guess = Integer.parseInt(guessStr);
        int target = (int) session.getAttribute("target");
        int attempts = (int) session.getAttribute("attempts") + 1;
        session.setAttribute("attempts", attempts);

        if (guess == target) {
            message = "You won in " + attempts + " tries!";
            session.invalidate(); // Reset game
        } else if (guess < target) {
            message = "Too low!";
        } else {
            message = "Too high!";
        }
    }
%>

<html>
<body>
    <h1>Guess the Number!</h1>
    <form method="get">
        <input type="number" name="guess" required>
        <button type="submit">Guess</button>
    </form>
    <p><strong><%= message %></strong></p>
</body>
</html>