<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h1>Welcome to My Landing Page</h1>
            <p>This is a sample landing page built with HTML and CSS.</p>
            <button>Learn More</button>
        </section>
        <section class="features">
            <h2>Features</h2>
            <div class="feature">
                <h3>Feature 1</h3>
                <p>Description of feature 1.</p>
            </div>
            <div class="feature">
                <h3>Feature 2</h3>
                <p>Description of feature 2.</p>
            </div>
            <div class="feature">
                <h3>Feature 3</h3>
                <p>Description of feature 3.</p>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 My Landing Page</p>
    </footer>
</body>
</html>



CSS (styles.css)

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 4em;
    text-align: center;
}

.hero h1 {
    font-size: 36px;
}

.features {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.feature {
    background-color: #f7f7f7;
    border: 1px solid #ddd;
    margin: 20px;
    padding: 20px;
    width: calc(33.33% - 20px);
}

.feature h3 {
    font-weight: bold;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

