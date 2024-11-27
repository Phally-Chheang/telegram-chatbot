import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot token
TOKEN = "8048524018:AAEbepb_WF4_SNf9n0h03UKLldhV6f_Xqxo"

# Load questions and answers from a JSON file
def load_qa_data(filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    return data["questions_and_answers"]

# Load data from qa.json file
qa_data = load_qa_data("qa.json")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! Welcome to the Python, CSS, and HTML Helper Bot.💞\n"
        "You can ask me questions about programming topics, and I’ll do my best to help.\n"
        "Type /help to see a list of commands and topics I can assist with!"
    )
# Define a greeting response
async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! 😊 How can I assist you with Python, CSS, or HTML today?")

# Help command to show detailed instructions and examples
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 *Help Guide* 🤖\n\n"
        "I’m here to answer your questions about programming topics including Python, CSS, and HTML.\n\n"
        "Please ask using lowercase letters, and I’ll respond if I know the answer!\n\n"
        "*Commands*\n"
        "/start - Start a conversation with me\n"
        "/help - View this help message\n"
        "/tutorial <topic> - Get a tutorial on a specific programming topic\n"
        "/codesnippet <language> - Get a code snippet for a specific language\n\n"
        "*How to Ask Questions*\n"
        "- 'What is Python?'\n"
        "- 'What is a CSS selector?'\n"
        "- 'Explain HTML attributes'\n\n"
        "Just type a question, and I’ll do my best to provide an answer! 😊"
    )

# Function to find the answer or provide a default response
def find_answer(user_question):
    user_question = user_question.lower()
    for qa in qa_data:
        if qa["question"].lower() in user_question:
            return qa["answer"]
    return "Sorry, we do not have information on that topic. Try asking another question!"

# Example API Call: Fetch tutorial for different topics
def get_tutorial(topic):
    tutorials = {
        "python": "Here is a tutorial about Python: https://www.w3schools.com/python/",
        "css": "Here is a tutorial about CSS: https://www.w3schools.com/css/",
        "html": "Here is a tutorial about HTML: https://www.w3schools.com/html/",
        "javascript": "Here is a tutorial about JavaScript: https://www.w3schools.com/js/",
        "django": "Here is a tutorial about Django: https://www.djangoproject.com/start/",
        "flask": "Here is a tutorial about Flask: https://flask.palletsprojects.com/en/2.2.x/tutorial/",
        "react": "Here is a tutorial about React: https://reactjs.org/tutorial/tutorial.html",
    }
    return tutorials.get(topic.lower(), "Sorry, I do not have a tutorial for that topic. Try another topic!")

# Example API Call: Fetch code snippet (mock example)
def get_code_snippet(language):
    snippets = {
        "python": """
        Here's a simple Python code snippet:
        ```python
        # Print Hello World
        print("Hello, World!")
        ```
        """,
        "css": """
        Here's a simple CSS code snippet:
        ```css
        /* Style for a paragraph */
        p {
            color: blue;
            font-size: 16px;
        }
        ```
        """,
        "html": """
        Here's a simple HTML code snippet:
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sample Page</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTML page.</p>
        </body>
        </html>
        ```
        """,
        "javascript": """
        Here's a simple JavaScript code snippet:
        ```javascript
        // Print Hello World
        console.log("Hello, World!");
        ```
        """,
        "java": """
        Here's a simple Java code snippet:
        ```java
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
        }
        ```
        """,
    
        "css_grid": """
        Here's a simple CSS Grid code snippet:
        ```css
        .container {
            display: grid;
            grid-template-columns: auto auto auto;
            gap: 10px;
        }

        .item {
            padding: 20px;
            background-color: lightgray;
            text-align: center;
        }
        ```
        """,    
    }

    return snippets.get(language.lower(), "Sorry, I do not have a code snippet for that language. Try another language!")

# Function to handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = find_answer(user_message)
    await update.message.reply_text(response)

# Handle tutorial command
async def tutorial_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        topic = context.args[0]
        tutorial_info = get_tutorial(topic)
        await update.message.reply_text(tutorial_info)
    else:
        await update.message.reply_text("Please specify a topic for the tutorial. Example: /tutorial python")

# Handle code snippet command
async def code_snippet_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        language = context.args[0]
        code_snippet = get_code_snippet(language)
        await update.message.reply_text(code_snippet)
    else:
        await update.message.reply_text("Please specify a language for the code snippet. Example: /codesnippet python")

# Main function to set up the bot and handlers
def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("tutorial", tutorial_command))
    application.add_handler(CommandHandler("codesnippet", code_snippet_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()
