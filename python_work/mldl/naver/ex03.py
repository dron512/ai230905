import pickle
from konlpy.tag import Okt

okt = Okt()
def tw_tokenizer(text):
    # 입력 인자로 들어온 text 를 형태소 단어로 토큰화 하여 list 객체 반환
    tokens_ko = okt.morphs(text)
    return tokens_ko

with open('saved_model.pickle','rb') as f:
    estimator = pickle.load(f)

with open('tfidf.pickle','rb') as f:
    tfidf = pickle.load(f)

test = []
test.append("이 영화 별로다")  # 0
test.append("이 영화 진짜 좋타")  # 1
test.append("이 영화 진짜 짱짱")  # 1
test.append("이 영화 진짜 싫어")  # 0
test.append("이 영화 진짜 좋음")  # 1
test.append("이 영화 진짜 구림")  # 0

print(test)

vec = tfidf.transform(test)
print(vec)

pred = estimator.predict(vec)
print(pred)

test_data = ['''
스파이더맨: 기대에 못 미치는 얽힌 이야기
"스파이더맨: 얽힌 이야기"는 이전 작품에서 기대되는 수준에 미치지 못하며, 전체적으로 분리된 느낌과 스파이더맨 시리즈에서 기대되는 일관성이 부족한 서사를 전달합니다. 톰 홀랜드의 아이코닉한 영웅 역할에도 불구하고, 영화는 자신의 발판을 찾는 데 어려움을 겪습니다.
주된 문제 중 하나는 특히 액션 장면에서의 CGI에 대한 지나친 의존으로, 때로는 지나치게 과장되고 인공적으로 느껴져 전체적인 시청 경험을 해치는 결과를 초래합니다. 슈퍼히어로 스펙터클을 강화하기 위한 시각 효과는 종종 과장되고 인공적으로 보여져 핵심적인 순간의 효과를 약화시킵니다.
줄거리는 새로운 요소를 도입하려는 노력에도 불구하고 부호화되어 있으며 명확한 목적을 수립하지 못합니다. 여러 악당의 등장은 이야기를 더욱 혼란스럽게 만들어 관객이 예상보다는 혼란스러운 감각을 남깁니다. 중요한 적의 부재는 긴장감을 떨어뜨려 스파이더맨 영화에서 기대되는 긴장감을 만들어내지 못합니다.
캐릭터 개발은 주요 문제로, 지원 캐릭터들은 제대로 활용되지 않으며 그들의 아크는 깊이가 부족합니다. 스파이더맨 시리즈의 특징인 유머는 종종 효과를 발휘하지 못하고 특정 장면에서 억지스럽게 느껴집니다. 이전 작품의 강점이었던 감동적인 감정은 뚜렷하게 부재해 캐릭터와 그들의 고뇌에서 관객을 멀리 떨어뜨립니다.
마무리로, "스파이더맨: 얽힌 이야기"는 매력적인 서사를 풀기에 어려움을 겪어 스파이더맨 영화 역사에 있어서도 기대에 미치지 못하는 실망스러운 작품입니다. 톰 홀랜드의 연기는 여전히 밝은 포인트이지만, 영화의 서술적인 결점과 시각적인 문제로 인해 이전 작품들의 높은 수준에 도달하지 못합니다. 이는 스파이더맨을 사랑하는 관객들에게는 얽히고 지루한 느낌을 남깁니다.
''','''
스파이더맨: 새로운 영웅의 탄생
"스파이더맨: 새로운 영웅의 탄생"은 기대 이상의 훌륭한 영화로, 액션, 유머, 그리고 감동적인 요소들이 완벽하게 어우러져 있습니다. 톰 홀랜드가 제시하는 스파이더맨의 훌륭한 연기는 관객들을 사로잡으며, 캐릭터에 새로운 측면을 부여합니다.
시각적인 효과는 군더더기 없이 훌륭하며, 특히 스파이더맨의 아종적인 기술을 강조하는 액션 장면에서는 놀라운 모습을 선사합니다. 국제적인 배경은 이야기에 새로운 동적인 요소를 더하며, 우리 친근한 이웃 슈퍼히어로를 그의 편안한 지역을 벗어나게 합니다.
이 작품을 돋보이게 하는 것 중 하나는 매력적이고 섬세하게 펼쳐지는 캐릭터들입니다. 제이크 질렌할의 미스테리오 역시 매력적으로 그려져 카리스마 넘치는 연기를 선보입니다. 특히 피터 파커와 그의 동급생들 간의 화기애애한 화합은 서사에 신뢰성과 공감을 더해줍니다.
"새로운 영웅의 탄생"은 유머와 감동을 적절히 조화시켜 진정한 웃음과 감동을 선사합니다. 작품의 전개와 전환은 관객을 자리에서 일어나게 만들며, 시작부터 끝까지 흥미진진한 여정을 제공합니다.
요약하자면, "스파이더맨: 새로운 영웅의 탄생"은 이전 작품에서 설정한 높은 기준을 완벽하게 충족시키며 그 이상을 제공합니다. 매력적인 이야기, 놀라운 시각적 효과, 그리고 매혹적인 캐스트로 이 영화는 오랜 팬들뿐만 아니라 마블 유니버스에 입문하는 이들에게도 꼭꼭 추천할 만한 작품입니다.
''']
vec = tfidf.transform(test_data)
pred = estimator.predict(vec)
print(pred)


























