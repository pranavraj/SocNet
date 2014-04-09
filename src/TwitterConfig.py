_consumer_key = ""
_consumer_secret =  ""

def get_consumer_key():
	if _consumer_key == "":
		raise Exceptions.KeyMissingException("consumer key missing")
	return _consumer_key

def get_consumer_secret():
	if _consumer_secret == "":
		raise Exceptions.KeyMissingException("consumer secret missing")
	return _consumer_secret


