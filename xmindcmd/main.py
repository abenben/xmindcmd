import xmindparser
from graphviz import Digraph


def create_graph_from_xmind(xmind_file):
    result = xmindparser.xmind_to_dict(xmind_file)
    sheet = result[0]
    g = Digraph('G', format='png')
    central_topic = sheet['topic']
    g.node(central_topic['title'], central_topic['title'])

    def add_subtopics(parent_title, topics):
        for topic in topics:
            g.node(topic['title'], topic['title'])
            g.edge(parent_title, topic['title'])
            if 'topics' in topic:
                add_subtopics(topic['title'], topic['topics'])

    add_subtopics(central_topic['title'], central_topic['topics'])
    return g


def save_graph_to_image(graph, output_file):
    graph.render(output_file, cleanup=True)


if __name__ == '__main__':
    xmind_file = "./example_xmind/sample.xmind"
    output_file = './output_image/output'

    graph = create_graph_from_xmind(xmind_file)
    save_graph_to_image(graph, output_file)
