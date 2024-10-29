Welcome, 
This has been the most dificult project i've done so far , stuggling in the fact that to become a good devoper my journey is just starting, this are the basics, at least I have been training them, because for bxecoming a good developer there are so many things that still needs to be learn , still I'm glad of the company Code Insitute provide me. is the best I can do and im happy and enjoy the process, thanks for taking the time to check what i've learn -J.D.C.

# ZenLift

### E-commerce webpage


![ZenLif](documentation/images/responsive.png)


___

ZenLift is a platform designed for fitness enthusiasts, offering products, personal coaching, and resources for a holistic fitness experience. Users can browse through training sessions, e-books, and a variety of men's and women's clothing. There’s also an extensive range of accessories, from gym and yoga equipment to vitamins and supplements, aiming to support wellness and fitness journeys. The site features perks like free delivery on larger orders and offers easy account management for a seamless shopping and training experience.

Link to live site - [https://zenlift-bb4261ea5a00.herokuapp.com/](https://zenlift-bb4261ea5a00.herokuapp.com/)

## Site Objectives

ZenLift offers users an all-in-one fitness platform with products, training, and wellness resources, supporting every step of a fitness journey. The site focuses on seamless navigation, holistic health, and quality service to inspire and support its community

Main objectives were:

- ### Promote Fitness Resources:

  Provide users with access to fitness products, training sessions, and e-books to support wellness goals.

- ### Enhance User Experience

  Offer smooth navigation and account management for a seamless shopping and training experience.

- ### Make use backend functionality

  Django’s powerful backend framework, the site allows users to create profiles, book reservations and buy items. This functionality provides a dynamic and interactive user experience, ensuring that users can easily engage with the content.

- ### Build Brand Trust

  Highlight benefits like free shipping on large orders and quality customer support to foster loyalty and satisfaction, featuring trusted payment options via Stripe for safe transactions.

# User Experience/UX

## Target Audience

- Fitness enthusiasts and individuals looking for personalized fitness guidance, resources, and high-quality products to support their wellness journeys.

## User Stories

### New Visitor Goals

- Clearly understand ZenLift’s mission and one-on-one coaching options.
- Discover personalized training programs and other site offerings.
- Sign up to track progress, access personal training sessions, and connect with expert coaches.

### Existing Visitor Goals

- Easily log in/out and manage their profiles.
- Access and schedule one-on-one training sessions, view personalized plans, and track fitness goals.
- Purchase recommended products, manage orders, and share feedback to engage with the community.

# Design Choices

## Colour Scheme

ZenLift’s color scheme uses vibrant and energetic hues to inspire motivation and energy in fitness. Neutral tones balance the layout, with bold accents on actionable items like buttons and links, enhancing visibility and encouraging engagement.

## Typography

The primary font is Montserrat, chosen for its modern, clean style and readability across all devices. A bolder, stylized font is used for the logo to add impact and brand recognition.

## Logo and Favicon

The logo and favicon capture ZenLift’s essence, featuring an icon symbolizing strength or growth, aligning with the fitness and wellness focus.

## Wireframes

- Conceptual wire frame made as sketchs

![Desktop Homepage Wireframe](documentation/images/mainpage.png)

- Desktop Search Wireframe

![Desktop Search Detail Wireframe](documentation/images/searchpage.png)

- Desktop Others Wireframe

![Desktop Search Detail Wireframe](documentation/images/others.png)

## Database Plan

The database plan for the "Street Seeker" app is straightforward, capturing essential information about users, bookings, checkout - payments, products, profiles -accounts. It outlines the type of data stored and indicates whether a field is a Primary or Foreign key where applicable.

<p align="center">
  <img src="documentation/images/databaseimage.png" alt="data-base">
</p>

### Entities and Attributes
1. User
- user_id (Primary Key): Integer, unique identifier for each user.
- username: String, unique username for login.
- email: String, unique email address.
- password: String, hashed password for security.
- first_name: String, user's first name.
- last_name: String, user's last name.
- is_active: Boolean, indicates if the user account is active.
- is_staff: Boolean, indicates if the user has admin privileges.
- date_joined: DateTime, timestamp of when the user account was created.
2. Trainer
- trainer_id (Primary Key): Integer, unique identifier for each trainer.
- name: String, full name of the trainer.
- expertise: String, area of expertise (e.g., strength training, nutrition).
- bio: Text, detailed biography of the trainer.
3. Appointment
- appointment_id (Primary Key): Integer, unique identifier for each appointment.
- user (Foreign Key): References the User table, linking to the user who booked the appointment.
- trainer (Foreign Key): References the Trainer table, linking to the trainer for the appointment.
- date: Date, the date of the appointment.
- time: Time, the time of the appointment.
- payment_status: Boolean, indicates whether payment has been made for the appointment.
4. UserProfile
- profile_id (Primary Key): Integer, unique identifier for each user profile.
- user (One-to-One Foreign Key): References the User table, linking to the user.
- default_phone_number: String, optional phone number for the user.
- default_street_address1: String, optional primary address.
- default_street_address2: String, optional secondary address.
- default_town_or_city: String, optional city or town.
- default_county: String, optional county.
- default_postcode: String, optional postal code.
- default_country: CountryField, user's default country (e.g., US).
5. Booking
- booking_id (Primary Key): Integer, unique identifier for each booking.
- user_profile (Foreign Key): References the UserProfile table, linking to the user's profile.
- appointment (Foreign Key): References the Appointment table, linking to the booked appointment.
- booking_date: DateTime, timestamp of when the booking was created.
- status: String, current status of the booking (e.g., confirmed, cancelled).
6. Order
- order_id (Primary Key): Integer, unique identifier for each order.
- order_number: String, unique order number generated using UUID.
- user_profile (Foreign Key): References the UserProfile table, linking to the user making the order.
- full_name: String, full name of the user.
- email: EmailField, user's email address.
- phone_number: String, user's phone number.
- country: CountryField, user's selected country.
- postcode: String, user's postal code.
- town_or_city: String, city or town of the user.
- street_address1: String, primary address.
- street_address2: String, optional secondary address.
- county: String, optional county.
- date: DateTime, timestamp of when the order was created.
- delivery_cost: Decimal, cost of delivery.
- order_total: Decimal, total cost of items ordered.
- grand_total: Decimal, total amount including delivery costs.
- original_bag: Text, serialized data of the user's cart.
- stripe_pid: String, unique identifier for the Stripe payment.
7. OrderLineItem
- lineitem_id (Primary Key): Integer, unique identifier for each line item.
- order (Foreign Key): References the Order table, linking to the corresponding order.
- product (Foreign Key): References the Product table, linking to the purchased product.
- product_size: String, size of the product (optional).
- quantity: Integer, quantity of the product ordered.
- lineitem_total: Decimal, total cost for the line item.

### Relationships

- A User can have one UserProfile.
- A User can book multiple Appointments.
- A Trainer can have multiple Appointments.
- A UserProfile can have multiple Bookings.
- Each Booking is associated with one Appointment.
- A UserProfile can have multiple Orders.
- Each Order can have multiple OrderLineItems.
- Each OrderLineItem is linked to a specific Product.

<p align="center">
  <img src="documentation/images/erd.png" alt="entity relationship">
</p>