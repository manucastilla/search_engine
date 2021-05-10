import re
from nltk.stem import RSLPStemmer


def stemmer(df):
    # https://www.datacamp.com/community/tutorials/stemming-lemmatization-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034358&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1001773&gclid=Cj0KCQjws-OEBhCkARIsAPhOkIaz_Gl4LR3zdQUBErnFXQNyFuad-t0PO-0q2KsTqKRgqSNQilO19TcaAgcmEALw_wcB
    # http://www.nltk.org/howto/portuguese_en.html
    stemmer = RSLPStemmer()
    ntxt = []
    for i in df.split():
        ntxt += [stemmer.stem(i)]
    return " ".join(ntxt)


def remove_symbols(df):
    # removes links
    # https://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url
    df = re.sub(r"[^@#\w\s]", "", df)
    #doesnt remove @, #
    df = re.sub(r"((http | https)\: \/\/)?[a-zA-Z0-9\.\/\?\: @\-_=  # ]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
                "", df)

    return df


def limpa_tudo(df):
    df = remove_symbols(df)
    df = stemmer(df)
    df = df.lower()
    return df
