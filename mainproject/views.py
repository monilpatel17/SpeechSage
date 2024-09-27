from django.shortcuts import render, HttpResponse
from openai import OpenAI
from django.http import JsonResponse
import json
from openai import OpenAI
import os

 

# Create your views here.
apikey = "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"



def index(request):
    return render(request, 'home.html')
    

os.environ["OPENAI_API_KEY"] = apikey
client = OpenAI()
def process_speech(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')

        # Send the text to OpenAI for interpretation
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "user will provide a passage that I spoke, and I would like you to correct any mistakes without focusing on writing conventions. Please identify and give me list of errors in grammar, pronunciation, and awkward phrasing as if it were spoken language. Don't bold anything."},
            {
                "role": "user",
                "content": f"{text}",
            }
        ]
    )

        # Extract the response text
        interpretation = response.choices[0].message.content
        return JsonResponse({'response': interpretation})

def howToUse(request):
    return render(request, 'howToUse.html')

def resource(request):
    return render(request, 'resource.html')