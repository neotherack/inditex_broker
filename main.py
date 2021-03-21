from website import Website
from sql import connect, create_table, insert_record, commit

config = ["elmundo.es","infolibre.es","laopinioncoruna.es","diariodesevilla.es","abc.es","lavanguardia.com","laverdad.es","ara.cat","diariodeleon.es","lavozdegalicia.es","latribunadealbacete.es","noticiasdegipuzkoa.eus","marca.com","as.com","sport.es","eleconomista.es","elpais.com","expansion.com","eldiario.es","economiadigital.es","nytimes.com","nbcnews.com","usatoday.com","foxnews.com","politico.com","dailynews.com","dailymail.co.uk","cnn.com","cnbc.com","economist.com"]

conn = connect()
if conn:
    create_table(conn)

    for url in config:
        site = Website(url)
        print(f"{site.url} processed")
        #print(site.clear_text[site.OFFSET:5000+site.OFFSET])
        insert_record(conn, site.url, "", site.clear_text, "")

    commit(conn)
    print("DB commit, you're done!")
else:
    print("Error on db access!")
