# This is only for development.
#
# In production, Flask is run by mod_wsgi, which imports the via wsgi.py.


from hyperion import app
app.debug=True
app.run(port=8080, host='0.0.0.0')
