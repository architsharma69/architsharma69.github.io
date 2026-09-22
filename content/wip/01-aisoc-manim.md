---
title: NUS AI Society Manim Generator
role: Main Handler        # or e.g. "Internship at Company X"
period: Ongoing
summary: An agent which generates short Manim-created GIFs to explain difficult concepts during seminar sessions
tags: [Python, Agentic AI]
image: assets/manim.png   # optional; delete this line for a card with no thumbnail
---

## Description
NUS AI Society is a research and engineering-focused community of students dedicated to exploring the frontier of Artificial Intelligence.

The Manim Generator is an agentic application that is meant to be deployed live during seminars and research-sharing sessions. It ingests the transcript, slides and other information, and outputs short animations generated using `Manim` - a Python Library used to create animations and simulations for educational content. These animations are meant to visualise abstract concepts taught during these seminar sessions, acting as visual aids for the audience.

## What I'm building
- An agent which reads the transcript, extracts pieces of it and puts them into buckets. Each bucket corresponds to one concept - one animation that will be outputted.
- Each bucket is promoted to a typed `AnimationPlan` - a structured input which will be sent to a manim animation generator (forked from an open source repository) to actualy create the animation.
- Along the way, we will inject another repository of Claude Skills, created for manim code generation.
- Following a number of rounds of iteration, including Human-In-The-Loop feedback, the final animation will outputted as either a GIF or as a slideshow which the speaker can manually traverse through.

## Tech stack
Python
