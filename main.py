import streamlit as st


introduction = """
Brief details about OpenAI DALL-E:

### What is OpenAI DALL-E?
DALL-E is a 12-billion parameter version of GPT-3 trained to generate images from text descriptions, using a dataset of text–image pairs². It can create original, realistic images and art from a text description¹. 

### What can OpenAI DALL-E do?
DALL-E has a diverse set of capabilities, including creating anthropomorphized versions of animals and objects, combining unrelated concepts in plausible ways, rendering text, and applying transformations to existing images². DALL-E 2 can make realistic edits to existing images from a natural language caption³.

### How does OpenAI DALL-E work?
DALL-E works by using a dataset of text–image pairs to learn how to generate images from textual descriptions². It uses a 12-billion parameter version of GPT-3².

### How can I use OpenAI DALL-E?
DALL-E is available in beta and can be used by signing up on their website⁵. 

```
Example usage:
Input: A cat made of sushi
Output: An image of a cat made out of sushi
```

Source: Conversation with Bing, 4/29/2023

- (1) DALL·E: Creating images from text - OpenAI. https://openai.com/research/dall-e.
- (2) DALL·E 2 - OpenAI. https://openai.com/product/dall-e-2.
- (3) DALL·E - OpenAI. https://labs.openai.com/.
- (4) DALL·E now available in beta - OpenAI. https://openai.com/blog/dall-e-now-available-in-beta/.
- (5) DALL·E 2 - openai.com. https://openai.com/product/dall-e-2?ref=promptsreport.com.
- (6) OpenAI API. https://platform.openai.com/docs/models/dall-e.

"""

# Define the pages
def page1():
    st.title("OpenAI DALL·E")
    st.markdown(introduction)

def page2():
    st.title("OpenAI DALL·E Image Generation")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")

def page3():
    st.title("OpenAI DALL·E Image Variation")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")

def page4():
    st.title("OpenAI DALL·E Image Editing")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")


pages = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4
}

# Create the selectbox in the sidebar
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Display the selected page
pages[page]()
