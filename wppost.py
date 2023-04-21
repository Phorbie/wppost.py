#!/usr/bin/env python

# wppost.py
# by Ben Steward
# Revision 0
# a shellscript to make writing wordpress posts using WP-CLI a lil easier.

import subprocess

# prompt user for post title
post_title = raw_input("Enter post title: ")

# prompt user for post content
post_content = raw_input("Enter post content: ")

# prompt user for publish status
post_status = raw_input("Post status (1. Draft 2. Published 3. Private): ")
post_status_options = ["", "draft", "publish", "private"]
selected_post_status = post_status_options[int(post_status)]

# Use wp-cli to create the post
create_post_command = 'wp post create --post_title="' + post_title + '" --post_content="' + post_content + '" --post_status="' + selected_post_status + '"'

subprocess.call(create_post_command, shell=True)
