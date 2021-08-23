# Exception as a flow control

* **EAFP:** easier to ask for forgiveness than permission
* **LBYL:** look before you leap



**Python example**: we make an assumption and we try if it works inside the `try`. If it doesn't work, then go `except` with the another branch. 

````python
# Python - EAFP

def search_contry( countries, country ):
	'''
	{ countries } is a dictionary.
	{ country } is the key.
	'''
    try:
        return countries[country]
    except KeyError:
		return None
````



**JavaScript example**: we confirm first if is valid our assumption, before try it

`````javascript
// JavaScript - LBYL

function search_country( countries, country ) {
    if (!Object.keys(countries).includes(country)) {
        return null
    }
    return countries[country]
}
`````

