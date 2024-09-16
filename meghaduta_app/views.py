from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')

def sandhi(request):
    # Read CSV file into a DataFrame
    df = pd.read_csv(settings.DATAPATH)
    # Convert the DataFrame to a list of dictionaries
    # data = df.to_dict(orient='records')
     # Select the first column values (assuming the column has a header)
    first_column_values = df.iloc[:, 0].tolist()  # Convert to a list    
    print(first_column_values)
    context={
        'data':first_column_values
    }
    return render(request,'sandhi.html',context)
def slokas(request):
    # Read CSV file into a DataFrame
    df = pd.read_csv(settings.DATAPATH)
    # Convert the DataFrame to a list of dictionaries
    # data = df.to_dict(orient='records')
     # Select the first column values (assuming the column has a header)
    first_column_values = df.iloc[:, 0].tolist()  # Convert to a list    
    context={
        'data':first_column_values
    }
    return render(request,'slokas.html',context)
def sandhiselected(request,id):
    return HttpResponse(id)
def slokaselected(request,uid):
    df = pd.read_csv(settings.DATAPATH)
     # Print the columns to see what's available
    print(df.columns)

      # Find the row where the UID matches the given uid
    row = df[df['UID'] == uid]
    # Check if the row exists
    if row.empty:
        raise Http404("Sloka not found")

    # Extract the 'sloka' and 'sandhi' values
    sloka = row.iloc[0]['sloka']
    sandhi = row.iloc[0]['sandhi']
    morph = row.iloc[0]['morph_analysis']  
    #----------------------------------------------------------
    import re
    # Remove specific punctuation if needed
    sloka = sloka.replace('।', '').replace('॥', '')
    sandhi = sandhi.replace('।', '').replace('॥', '')
    sandhi = sandhi.replace("\n", " ")

    # Split the cleaned text
    sloka_splitted = re.split(r'\s+', sloka)
    sandhi_splitted = re.split(r'\s+', sandhi)
    #----------------------------------------------------------
    # Pass these values to the context
    # sloka_splitted=sloka.split(" ")
    # sandhi_splitted=sandhi.split(" ")

    # Combine the lists into a dictionary
    word_dict = dict(zip(sloka_splitted, sandhi_splitted))
    context = {
        'sloka': sloka,
        'sandhi': sandhi,
        'sloka_splitted':sloka_splitted,
        'sandhi_splitted':sandhi_splitted,
        'word_dict':word_dict,
        'morph':morph,
    }
    print(sandhi_splitted)

    return render(request,'slokaprocess.html',context)   
    return HttpResponse(sloka)
def samasam(request):
    return render(request,'samasam.html')
def user_guide(request):
    return render(request,'user_guide.html')