from dataclasses import dataclass


@dataclass
class SearchData:
    search_text: str
    expected_search_text: str
    expected_article_description: str


search_data = SearchData(
    search_text='Python',
    expected_search_text='Python',
    expected_article_description='Topics referred to by the same term'
)
