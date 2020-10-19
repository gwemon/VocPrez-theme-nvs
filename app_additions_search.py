# ROUTE search
@app.route("/search")
def search():
    vs = [(k.replace("http://vocab.nerc.ac.uk/collection/", "").replace("http://vocab.nerc.ac.uk/scheme/", "").replace("/current/", ""), v.title) for k, v in g.VOCABS.items()]
    logging.info(vs)
    return render_template(
        "search.html",
        vocabs=sorted(vs, key=lambda tup: tup[0])
    )
# END ROUTE search
