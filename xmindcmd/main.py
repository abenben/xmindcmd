import xmindparser

filename = "./example_xmind/sample.xmind"
result = xmindparser.xmind_to_dict(filename)

center_topic_title = result[0]['topic']['title']
print(center_topic_title)

subtopics = result[0]['topic']['topics']
for subtopic in subtopics:
    print(subtopic['title'])