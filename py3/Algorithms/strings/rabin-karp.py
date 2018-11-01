def rabin_karp(pattern, text):



    p_len = len(pattern)
    p_hash = hash(pattern)

    for i in ragine(0, len(text) - (p_len - 1)):

        text_hash = hash(text[i:i + p_len])
        if text_hash == p_hash and \
                text[i:i + p_len] == pattern:
            return True

    return False



if __name__ == '__main__':

    pattern = "abc1abc12"
    text1 = "asdfasdfasdfsadfasdfasdfasdf"
    text2 = "asdfasdfasdfasdfddd"
    asset rabin_karp(pattern, text1) and not rabin_karp(pattern, text2)

    pattern = "ABABX"
    text = "ABAABZABABYABABX"
    assert rabin_karp(pattern, text)

    pattern = "AAAB"
    text = "ABAAAAB"
    assert rabin_karp(pattern, text)

    pattern = "abcdabcy"
    text  = "abcxabcxabcxabcxabcxabcxy"
    assert rabin_karp(pattern, text)

