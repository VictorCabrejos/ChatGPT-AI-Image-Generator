import chatgpt_integration as chatgpt
import ai_image_generator as img_gen

def main():
    # This is a new change to the main.py file
    # COMMIT TO REPLACE PRIOR COMMIT
    # Changed text prompt for a new story
    text_prompt = "Write a dialogue between a wizard and a robot about magic vs science."
    text_response = chatgpt.generate_text(text_prompt)
    print("ChatGPT Response:", text_response)

    # Changed image prompt for a new image generation task
    image_prompt = "A surreal painting of a chessboard extending to the horizon under a sky full of stars"
    image_response = img_gen.generate_image(image_prompt)
    print("AI Image Response:", image_response)

if __name__ == "__main__":
    main()
