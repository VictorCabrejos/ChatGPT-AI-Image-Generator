import chatgpt_integration as chatgpt
import ai_image_generator as img_gen

def main():
    text_prompt = "Write a short story about a lost treasure."
    text_response = chatgpt.generate_text(text_prompt)
    print("ChatGPT Response:", text_response)

    image_response = img_gen.generate_image("Illustration of a lost treasure")
    print("AI Image Response:", image_response)

if __name__ == "__main__":
    main()
