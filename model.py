import json
import openai

with open('congig.json', 'r') as f:
  config=json.load(f)

model=config['MODEL_NAME']
openai.api_key =config['API_KEY']

def inference_gpt(model, prompt):
  return openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model='text-davinci-003')["choices"][0]["text"].strip(" \n")



def solution(file, question, model):
#   reader = PdfReader(file_path)
  reader=file
  text=[]
  for i in range(len(reader.pages)):
      page = reader.pages[i]
      text.append(page.extract_text())
  answer=[]
  for i in text:
    prompt=config['PROMPT_SINGLE']+f'Context:{i} Q:{question} A:'
    result=inference_gpt(model, prompt)
    answer.append(result)
    #print(result)
  final_answers = [ans for ans in answer if ans not in ["I don't know.","I don't know"]]

  print(final_answers)
  if len(final_answers)>1:
    print('hi')
    prompt=f'Keeping the context of: "{question}" pick two or three importance sentences from list: {final_answers}'
    return inference_gpt(model, prompt)
  else:
    return final_answers