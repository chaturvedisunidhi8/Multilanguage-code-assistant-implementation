##to create your own custom model which will use codellama so for that let's create a modelfile
import requests ## to make request bcz our codeguru running in backend so we need to connect to it with api
import json ## to parse the response
import gradio as gr ## to create a web interface or frontend

url="http://localhost:11434/api/generate"        ##llama has a REST API for running and managing models,get the url from github of ollama website
headers={"Content-Type":"application/json"}  ##specify the content type as json

history=[]  ##to store the chat history
def generate_response(prompt):
    history.append(prompt)  ##append the user prompt to the history
    final_prompt = "\n".join([str(item) for item in history])
 ##to store the final prompt
 

    data={                                        #create body of the request
     "model":"codeguru",
     "prompt":final_prompt,
     "stream":False ## to not get unnecessary values

    }

    response=requests.post(url,headers=headers,data=json.dumps(data))  ##make a post request to the url with headers and body, we want to convert data in the from json

    if response.status_code==200:  ##if the response is successful
        response=response.text
        data=json.loads(response)  ##load the response in json format
        actual_response=data['response']
        return actual_response
    else:
        print("Error:",response.text)
    ##so this was the backendpart now we will create the frontend part using gradio

interface=gr.Interface(
        fn=generate_response,  ##function to be called when user submits a prompt
        inputs=gr.Textbox(lines=4,placeholder="Enter your prompt here..."),  ##input textbox for user prompt
        #outputs="text"  ##output textbox to display the response
        # outputs=gr.Textbox(label="💡 Model Response", lines=12, interactive=False)
        outputs=gr.Textbox(lines=15))
interface.launch()  ##to launch the interface and share it with others
## to run write python app.py
##conda activate venv in case of folder38
##to check codeguru is running or not ollama list
##to stop codeguru ollama stop codeguru
                               




