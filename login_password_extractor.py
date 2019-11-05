# PSD Organizer

FILE_HEADER = "url,username,password,extra,name,grouping,fav"
REGISTRY_START = "http"

SUBJECT_DELIMITATOR = "============================================="

APP_HEADER = "APP"
BUSINESS_HEADER = "BUSINESS"
SHOPPING_HEADER = "SHOPPING"
FINANCAS_HEADER = "FINANÇAS"
EDUCATION_HEADER = "EDUCATION"
CORRETORAS_HEADER = "CORRETORAS"
PONTOS_MILHAS_HEADER = "PONTOS/MILHAS"
EMAIL_HEADER = "EMAIL"
MOBILE_HEADER = "MOBILE"
CARTAO_CREDITO_HEADER = "CARTÃO CREDITO"
SOCIAL_HEADER = "SOCIAL"
CRIPTO_HEADER = "CRIPTOMOEDAS"

INPUT_FILE_NAME = "login.txt"
OUTPUT_FILE_NAME = "login_extracted.txt"

applicationList = []
businessList = []
shoppingList = []
financasList = []
educationList = []
corretorasList = []
pontosMilhasList = []
emailList = []
mobileList = []
cartaoCreditoList = []
socialList = []
criptomoedasList = []

allSubjectsList = [applicationList, \
                    businessList, \
                    shoppingList, \
                    financasList, \
                    educationList, \
                    corretorasList, \
                    pontosMilhasList, \
                    emailList, \
                    mobileList, \
                    cartaoCreditoList, \
                    socialList, \
                    criptomoedasList]

def initializeListContents():
    applicationList.append(SUBJECT_DELIMITATOR + "\n")    
    applicationList.append(APP_HEADER + "\n")    
    applicationList.append(SUBJECT_DELIMITATOR + "\n")

    businessList.append(SUBJECT_DELIMITATOR + "\n")    
    businessList.append(BUSINESS_HEADER + "\n")    
    businessList.append(SUBJECT_DELIMITATOR + "\n")

    shoppingList.append(SUBJECT_DELIMITATOR + "\n")    
    shoppingList.append(SHOPPING_HEADER + "\n")    
    shoppingList.append(SUBJECT_DELIMITATOR + "\n")

    financasList.append(SUBJECT_DELIMITATOR + "\n")    
    financasList.append(FINANCAS_HEADER + "\n")    
    financasList.append(SUBJECT_DELIMITATOR + "\n")

    educationList.append(SUBJECT_DELIMITATOR + "\n")    
    educationList.append(EDUCATION_HEADER + "\n")    
    educationList.append(SUBJECT_DELIMITATOR + "\n")

    corretorasList.append(SUBJECT_DELIMITATOR + "\n")    
    corretorasList.append(CORRETORAS_HEADER + "\n")    
    corretorasList.append(SUBJECT_DELIMITATOR + "\n")

    pontosMilhasList.append(SUBJECT_DELIMITATOR + "\n")    
    pontosMilhasList.append(PONTOS_MILHAS_HEADER + "\n")    
    pontosMilhasList.append(SUBJECT_DELIMITATOR + "\n")

    emailList.append(SUBJECT_DELIMITATOR + "\n")    
    emailList.append(EMAIL_HEADER + "\n")    
    emailList.append(SUBJECT_DELIMITATOR + "\n")

    mobileList.append(SUBJECT_DELIMITATOR + "\n")    
    mobileList.append(MOBILE_HEADER + "\n")    
    mobileList.append(SUBJECT_DELIMITATOR + "\n")

    cartaoCreditoList.append(SUBJECT_DELIMITATOR + "\n")    
    cartaoCreditoList.append(CARTAO_CREDITO_HEADER + "\n")    
    cartaoCreditoList.append(SUBJECT_DELIMITATOR + "\n")

    socialList.append(SUBJECT_DELIMITATOR + "\n")    
    socialList.append(SOCIAL_HEADER + "\n")    
    socialList.append(SUBJECT_DELIMITATOR + "\n")

    criptomoedasList.append(SUBJECT_DELIMITATOR + "\n")    
    criptomoedasList.append(CRIPTO_HEADER + "\n")    
    criptomoedasList.append(SUBJECT_DELIMITATOR + "\n")


def extractAndStoreTokens(line):    
    tokens = line.split(",")

    if(len(tokens) != 7):        
        return

    auxList = []
    subjectKey = tokens[5].upper() + "\n"    

    for subList in allSubjectsList:        
        if(subList[1] == subjectKey):
            auxList = subList
            break

    auxList.append(tokens[4].upper() + "\n")
    auxList.append(tokens[0] + "\n")
    auxList.append(tokens[1] + "\n")
    auxList.append(tokens[2] + "\n")
    auxList.append("\n")
 
def printListContents():
    for subList in allSubjectsList:
        for item in subList:
            print(item)


def storeLists()            :
    writer = open(OUTPUT_FILE_NAME, "w")

    for subList in allSubjectsList:
        if(len(subList) > 3):
            for item in subList:
                writer.write(item)

    writer.close()


initializeListContents()

file = open(INPUT_FILE_NAME, "r")

for line in file:
    line = line.strip()
    if(line.startswith(REGISTRY_START)):
        extractAndStoreTokens(line)

storeLists()

print(OUTPUT_FILE_NAME + " generated successfully!")

file.close()