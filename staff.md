---
layout: page
title: Staff
has_children: false
nav_order: 10
description: Listing of all the course staff members.
---

# Staff

<!-- Contact information for the course staff. -->

---

## Course Instructor

{% assign instructors = site.staffers | where: 'role', 'Course Instructor' %}

{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

---

## Teaching Assistants

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

<!-- ---

## Undergraduate Learning Assistants

{% assign undergraduate_learning_assistants = site.staffers | where: 'role', 'Undergraduate Learning Assistant' %}
{% assign num_undergraduate_learning_assistants = undergraduate_learning_assistants | size %}
{% if num_undergraduate_learning_assistants != 0 %}

{% for staffer in undergraduate_learning_assistants %}
{{ staffer }}
{% endfor %}
{% endif %} -->

<!-- ---

## Help Room Schedule and Hours

Monday | 5:00pm to 6:00pm (EST)
Tuesday | 5:00pm to 6:00pm (EST)
Wednesday | 4:00pm to 5:00pm (EST)
Thursday | 5:00pm to 6:00pm (EST)
Friday | 5:00pm to 6:00pm (EST)
Saturday | No help room
Sunday | No help room

[Zoom link](https://msu.zoom.us/s/93419919566)

* Meeting ID: 934 1991 9566
* Passcode: 123456 -->