import chatgpt_integration as chatgpt
import ai_image_generator as img_gen

def main():
    text_prompt = "Write a poem about a mysterious forest."
    text_response = chatgpt.generate_text(text_prompt)
    print("ChatGPT Response:", text_response)

    image_prompt = "A futuristic cityscape at sunset"
    image_response = img_gen.generate_image(image_prompt)
    print("AI Image Response:", image_response)

if __name__ == "__main__":
    main()