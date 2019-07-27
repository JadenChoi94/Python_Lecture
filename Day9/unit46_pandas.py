# 데이터로 그래프 그리기
# % matplotlib inline을 설정하면 matplotlib.pyplot의 show 함수를 호출하지 않아도 \
# 주피터 노트북 안에서 그래프가 표시됨

% matplotlib
inline
import pandas as pd  # 데이터를 저장하고 처리하는 패키지
import matplotlib as mpl  # 그래프를 그리는 패키지
import matplotlib.pyplot as plt  # 그래프를 그리는 패키지

# csv 파일을 읽어서 DataFrame 객체로 만듦. 인덱스 컬럼은 point로 설정
df = pd.read_csv('weather.csv', index_col='point')
df  # df 표시

# csv 파일을 읽어서 DataFrame 객체로 만듦. 인덱스 컬럼은 point로 설정, 인코딩은 euc-kr로 설정
df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')

# 특별시 광역시만 모으기

# 특별시, 광역시만 모아서 DataFrame 객체로 만듦
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
city_df    # city_df 표시
df.loc['서울']

# 특별시, 광역시만 그래프 그리기
# Windows 한글 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)  # x축 정보 표시
ax.set_ylabel('기온/습도', fontsize=12)  # y축 정보 표시
ax.legend(['기온', '습도'], fontsize=12)  # 범례 지정

# 소스 코드 살펴보기
# Windows 한글 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# plot 메서드로 그래프 그리기
# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)

ax.set_xlabel('도시', fontsize=12)          # x축 정보 표시
ax.set_ylabel('기온/습도', fontsize=12)     # y축 정보 표시

ax.legend(['기온', '습도'], fontsize=12)    # 범례 지정

%matplotlib inline
#  show 메서드로 그래프를 표시하기
plt.show()    # %matplotlib inline을 지정하지 않았거나 IDLE, 파이썬 인터프리터에서
              # 그래프를 표시하려면 matplotlib.pyplot의 show 함수 호출

# DataFrame 사용하기

city_df['temperature']
city_df.temperature

city_df.temperature.argmax()
city_df.temperature.argmin()

city_df.loc[city_df.temperature.argmax()]
city_df.loc[city_df.temperature.argmin()]


