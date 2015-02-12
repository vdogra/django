#ONE TO ONE RELATION For Extending Default User Model

This module shows one of the methods to extend the default User model of Django. A new model is introduced which
contains extra information related to a particular type of user and is specific to an application.

#Concepts implemented

- OneToOne relation between new model and default User model of Django
- Customizing admin interface to include information stored in new model

#Notes

Using this method of extension we're able to inherit the properties of default Django model as well as add our custom
properties. Though it results in additional queries or joins to retrieve related information.