def apply_style(style, response):
    if style == "kid":
        return "🧒 As a kid: " + response.replace("difficult", "hard").replace("moreover", "also")
    elif style == "teacher":
        return "👨‍🏫 As a physics teacher: " + response + " Remember, always think critically!"
    else:
        return "🧠 Default style: " + response
