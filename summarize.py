from sumy.nlp.tokenizers import Tokenizer


from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.reduction import ReductionSummarizer

LANGUAGE = "vietnam"
stemmer = Stemmer(LANGUAGE)

def lexrank_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string((text), Tokenizer(language))
    summarizer_LexRank = LexRankSummarizer(stemmer)
    summarizer_LexRank.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_LexRank(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)

def lsa_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string((text), Tokenizer(language))
    summarizer_lsa = Summarizer(stemmer)
    summarizer_lsa.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_lsa(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)


def luhn_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer_luhn = LuhnSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_luhn(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)

def edmundson_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer_luhn = EdmundsonSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(language)
    words = ("computing", "learning", "mobile")
    summarizer_luhn.bonus_words = words

    words = ("another", "and", "some", "next",)
    summarizer_luhn.stigma_words = words

    words = ("another", "and", "some", "next",)
    summarizer_luhn.null_words = words

    sentences = []
    for sentence in summarizer_luhn(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)

def sumbasic_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer_luhn = SumBasicSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_luhn(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)

def kl_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer_luhn = KLSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_luhn(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)

def textrank_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer_luhn = TextRankSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_luhn(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)

def reduction_summarizer(text, stemmer, language, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer_luhn = ReductionSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(language)
    sentences = []
    for sentence in summarizer_luhn(parser.document, sentences_count):
        a = sentence
        sentences.append(str(a))
    return "\n".join(sentences)


def summarize(text, stemmer = stemmer, language = 'vietnam', sentences_count = 2, sum_index = 0):
    def switch(sum_index):
        switcher={
            0: textrank_summarizer(text, stemmer, language, sentences_count),
            1: lexrank_summarizer(text, stemmer, language, sentences_count),
            2: luhn_summarizer(text, stemmer, language, sentences_count),
            3: reduction_summarizer(text, stemmer, language, sentences_count),
            4: sumbasic_summarizer(text, stemmer, language, sentences_count),
            5: kl_summarizer(text, stemmer, language, sentences_count),
            6: edmundson_summarizer(text, stemmer, language, sentences_count)
        }
        return switcher.get(sum_index)
    return switch(sum_index)