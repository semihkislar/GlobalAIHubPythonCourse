score = 0
questions = [
    {'question': 'Tarihin sıfır noktası olarak bilinen, insanlık tarihinin ilk somut kalıntılarının bulunduğu Göbekli tepe hangi ilimizdedir?',
     'answer': 'şanlıurfa'},
    {'question': 'Dünyanın en büyük deniz kazalarından biri olarak tarihe geçti. 1912 yılında 1.550 kişiye mezar olan ünlü transatlantiğin adı nedir?',
     'answer': 'titanik'
     },
    {'question': 'Haberleşmenin eski dildeki adı nedir? ',
     'answer': 'muhabere'},
    {'question': 'Osmanlıda şehzadelerin özel hocası, eğitmenlerine verilen isim',
     'answer': 'lala'},
    {'question': 'Şehzadelerin hükümdar olarak tahta çıkması anına törenlerine ne ad verilir',
     'answer': 'cülus'}
]

print('Welcome the best Competition on the world!')

for i in questions:
    print(i['question'])
    answer = input('Please input your answer.....:')
    if(answer.lower() == i['answer']):
        print('Congratulations!!!!')
        score += 10
    else:
        print('Im so soo soorryy! Wrong Answer!')

if score < 50:
    print('Hey Man! You are the WINNER')
else:
    print('LOOSER!')
