def emojis(message):
    words = message.split(" ")
    emojis = {
        ":)": "\U0001F600",
        ":(": "☹",
        ";)": "😉",
        ":D": "😱",
        "$_$": "🤑"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emojis(message))