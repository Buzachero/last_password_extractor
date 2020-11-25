# PSD Organizer

FILE_HEADER = "url,username,password,totp,extra,name,grouping,fav"
REGISTRY_START = "http"
DELIMITER = ","
FILE_HEADER_SIZE = len(FILE_HEADER.split(DELIMITER))

# HEADER INDEXES
URL_INDEX = 0
USERNAME_INDEX = 1
PASSWORD_INDEX = 2
SITE_NAME_INDEX = 5
SUBJECT_KEY_INDEX = 6


# SUBJECT CONSTANTS

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
    tokens = line.split(DELIMITER)

    if(len(tokens) != FILE_HEADER_SIZE):     
        print('Line WITHOUT header pattern: %s' % (line))
        return

    auxList = []
    subjectKey = tokens[SUBJECT_KEY_INDEX] 
    subjectKeyUpperCase = str(subjectKey).upper()

    for subList in allSubjectsList:        
        if(subjectKeyUpperCase in subList[1]):
            auxList = subList
            break

    siteName = tokens[SITE_NAME_INDEX]
    url = tokens[URL_INDEX] 
    username = tokens[USERNAME_INDEX]
    password = tokens[PASSWORD_INDEX]

    auxList.append(siteName.upper())
    auxList.append("\n")
    auxList.append(url)
    auxList.append("\n")
    auxList.append(username)
    auxList.append("\n")
    auxList.append(password)
    auxList.append("\n\n")    
 
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
    else:
        print('Line WITHOUT \'%s\': %s' % (REGISTRY_START, line))

storeLists()

print(OUTPUT_FILE_NAME + " generated successfully!")

file.close()
