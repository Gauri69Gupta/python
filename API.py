#1. Difference between JSON and XML files.
NO.	             JSON	                                        XML
1)	JSON stands for JavaScript	                XML stands for eXtensible
        Object Notation.                                Markup Language.
2)	JSON is simple to read and write.	        XML is less simple than JSON.
3)	JSON is easy to learn.	                        XML is less easy than JSON.
4)	JSON is data-oriented.	                        XML is document-oriented.
5)	JSON doesn’t provide display capabilities.	XML provides the capability to display data because it is a markup language.
6)	JSON supports array.	                        XML doesn’t support array.
7)	JSON is less secured than XML.	                XML is more secured.
8)	JSON files are more human readable than XML.	XML files are less human readable.
9)	JSON supports only text and number data type.	XML support many data types
                                                        such as text, number, images, charts,
                                                        graphs etc. Moreover, XML offeres
                                                        options for transferring the
                                                        format or structure of the
                                                        data with actual data.

print("Question2")
import socket
addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('facebook.com')
print(addr1)
print(addr2)
print('\n')

#3. How HTTP works like..?
GET method
-->GET requests are the most common and widely used methods in APIs and
websites. Simply put, the GET method is used to retreive data from a server
at the specified resource. For example, say you have an API with a /users
endpoint. Making a GET request to that endpoint should return a list of all
available users.

Since a GET request is only requesting data and not modifying any resources,
it's considered a safe and idempotent method.

POST method
-->The simplest example is a contact form on a website. When you fill out the
inputs in a form and hit Send, that data is put in the response body of the
request and sent to the server. This may be JSON, XML, or query parameters
(there's plenty of other formats, but these are the most common).

It's worth noting that a POST request is non-idempotent. It mutates data on
the backend server (by creating or updating a resource), as opposed to a GET
request which does not change any data

PUT method
-->Simlar to POST, PUT requests are used to send data to the API to create or
update a resource. The difference is that PUT requests are idempotent. That is,
calling the same PUT request multiple times will always produce the same result.
In contrast, calling a POST request repeatedly make have side effects of
creating the same resource multiple times.

DELETE method
-->The DELETE method is exactly as it sounds: delete the resource at the
specified URL. This method is one of the more common in RESTful APIs so it's
good to know how it works.

If a new user is created with a POST request to /users, and it can be
retrieved with a GET request to /users/{{userid}}, then making a DELETE
request to /users/{{userid}} will completely remove that user.

#4. What is the difference between library and API..?
A library is a chunk of code designed for reuse that is typically installed
locally. A library is most often wrapped in an API that defines the
functionality the library provides and how to use it.

Technically speaking, the term API refers to an interface that doesn't
need to have an implementation. However, when people speak of an API they are
usually referring to a reusable library or service. Where a library is used
as a package of code, a service is a running system that provides
functionality to other systems and applications.
