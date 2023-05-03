import streamlit as st

introduction = """
Brief details about OpenAI DALL-E:

### What is OpenAI DALL-E?

DALL-E is a 12-billion parameter version of GPT-3 trained to generate images from text 
descriptions, using a dataset of text–image pairs². It can create original, realistic 
images and art from a text description¹. 

### What can OpenAI DALL-E do?

DALL-E has a diverse set of capabilities, including creating anthropomorphized versions 
of animals and objects, combining unrelated concepts in plausible ways, rendering text, 
and applying transformations to existing images². DALL-E 2 can make realistic edits to 
existing images from a natural language caption³.

### How does OpenAI DALL-E work?
DALL-E works by using a dataset of text–image pairs to learn how to generate images 
from textual descriptions². It uses a 12-billion parameter version of GPT-3².

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