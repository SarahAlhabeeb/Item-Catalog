#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///applecategory.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Dummy user
user1 = User(name="Dummy User", email="default@gmail.com",
             picture="https://pbs.twimg.com/profile_images/2671170543/"
                     "18debd694829ed78203a5a36dd364160_400x400.png")
session.add(user1)
session.commit()

# Menu for Mac
category1 = Category(title="Mac")

session.add(category1)
session.commit()

Item2 = Item(title="MacBook",
             description="Consumer ultra-thin, ultra-portable notebook, "
                         "introduced in 2006 and relaunched in 2015.",
             user=user1, category=category1)

session.add(Item2)
session.commit()


Item1 = Item(title="MacBook Air",
             description="Consumer ultra-thin, ultra-portable"
                         " notebook, introduced in 2008.",
             user=user1, category=category1)

session.add(Item1)
session.commit()

Item2 = Item(title="MacBook Pro",
             description="Professional notebook, first introduced in "
                         "2006. More power. More performance. More pro.",
             user=user1, category=category1)

session.add(Item2)
session.commit()

Item3 = Item(title="iMac",
             description="Consumer all-in-one desktop computer,"
                         " first introduced in 1998.",
             user=user1, category=category1)

session.add(Item3)
session.commit()

Item4 = Item(title="iMac Pro", description="Power to the pro.",
             user=user1, category=category1)

session.add(Item4)
session.commit()

# Menu for iPad
category2 = Category(title="iPad")

session.add(category2)
session.commit()


Item1 = Item(title="iPad Pro NEW",
             description="All new. All screen. All powerful.",
             user=user1, category=category2)

session.add(Item1)
session.commit()

Item2 = Item(title="iPad Pro 10.5",
             description="10.5 inch Retina display "
                         "with ProMotion technology and True Tone",
             user=user1, category=category2)

session.add(Item2)
session.commit()

Item3 = Item(title="iPad 9.7",
             description="Like a computer. Unlike any computer.",
             user=user1, category=category2)

session.add(Item3)
session.commit()

Item4 = Item(title="iPad Mini 4 ",
             description="iPad mini 4 puts uncompromising performance and "
                         "potential in your hand. "
                         "Thinner & lighter than ever before. ",
             user=user1, category=category2)

session.add(Item4)
session.commit()


# Menu for iPhone
category3 = Category(title="iPhone")

session.add(category3)
session.commit()


Item1 = Item(title="iPhone Xs",
             description="Super Retina in two sizes including the "
                         "largest display ever on an iPhone."
                         " Even faster Face ID.",
             user=user1, category=category3)

session.add(Item1)
session.commit()

Item2 = Item(title="iPhone XR",
             description="All-screen design. Longest battery "
                         "life ever in an iPhone."
                         " Fastest performance. Water and splash resistant.",
             user=user1, category=category3)

session.add(Item2)
session.commit()

Item3 = Item(title="iPhone 8",
             description=" It is the eleventh generation of the iPhone."
                         " It was announced on September 12, 2017,"
                         " alongside the higher-end iPhone X.",
             user=user1, category=category3)

session.add(Item3)
session.commit()

Item4 = Item(title="iPhone 7",
             description=" It is the tenth generation of the iPhone."
                         " It was announced on September 7, 2016, "
                         "at the Bill Graham Civic Auditorium in San "
                         "Francisco by Apple CEO Tim Cook.",
             user=user1, category=category3)

session.add(Item4)
session.commit()


# Menu for watch
category4 = Category(title="Watch")

session.add(category4)
session.commit()


Item1 = Item(title="Apple Watch Series 4",
             description="The largest Apple Watch display yet."
                         " New electrical heart sensor."
                         " Re-engineered Digital Crown with haptic feedback.",
             user=user1, category=category4)

session.add(Item1)
session.commit()

Item2 = Item(title="Apple Watch Nike+",
             description="Apple Watch Nike+ is the perfect"
                         " running partner with the Nike Run Club app.",
             user=user1, category=category4)

session.add(Item2)
session.commit()

Item3 = Item(title="Apple Watch Hermes",
             description="A partnership based on parallel thinking,"
                         " singular vision, and mutual regard continues"
                         " with a fresh new expression.",
             user=user1, category=category4)

session.add(Item3)
session.commit()

Item4 = Item(title="Apple Watch Series 3",
             description="Monitor your health. Track your workouts."
                         " Get the motivation you need to achieve"
                         " your fitness goals. Now starting at $279",
             user=user1, category=category4)

session.add(Item4)
session.commit()

print("added menu items!")
