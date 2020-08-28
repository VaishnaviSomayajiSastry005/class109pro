import pandas as pd 
import statistics
import csv
df=pd.read_csv('marks.csv')
genderList=df['gender'].to_list()
raceList=df['race/ethnicity'].to_list()
educationList=df['parental level of education'].to_list()
lunchList=df['lunch'].to_list()
testList=df['test preparation course'].to_list()
mathList=df['math score'].to_list()
readingList=df['reading score'].to_list()
writingList=df['writing score'].to_list()

gender_mean=statistics.mean(genderList)
race_mean=statistics.mean(raceList)
education_mean=statistics.mean(educationList)
lunch_mean=statistics.mean(lunchList)
test_mean=statistics.mean(testList)
math_mean=statistics.mean(mathList)
reading_mean=statistics.mean(readingList)
writing_mean=statistics.mean(writingList)

gender_median=statistics.median(genderList)
race_median=statistics.median(raceList)
education_median=statistics.median(educationList)
lunch_median=statistics.median(lunchList)
test_median=statistics.median(testList)
math_median=statistics.median(mathList)
reading_median=statistics.median(readingList)
writing_median=statistics.median(writingList)

gender_mode=statistics.mode(genderList)
race_mode=statistics.mode(raceList)
education_mode=statistics.mode(educationList)
lunch_mode=statistics.mode(lunchList)
test_mode=statistics.mode(testList)
math_mode=statistics.mode(mathList)
reading_mode=statistics.mode(readingList)
writing_mode=statistics.mode(writingList)

print('mean,median and mode of gender is {}, {} and {} respectively'.format(gender_mean,gender_median,gender_mode))
print('mean,median and mode of race is {}, {} and {} respectively'.format(race_mean,race_median,race_mode))
print('mean,median and mode of education is {}, {} and {} respectively'.format(education_mean,education_median,education_mode))
print('mean,median and mode of lunch is {}, {} and {} respectively'.format(lunch_mean,lunch_median,lunch_mode))
print('mean,median and mode of test is {}, {} and {} respectively'.format(test_mean,test_median,test_mode))
print('mean,median and mode of math is {}, {} and {} respectively'.format(math_mean,math_median,math_mode))
print('mean,median and mode of reading is {}, {} and {} respectively'.format(reading_mean,reading_median,reading_mode))
print('mean,median and mode of writing is {}, {} and {} respectively'.format(writing_mean,writing_median,writing_mode))

gender_stdev=statistics.stdev(gendertList)
race_stdev=statistics.stdev(raceList)
education_stdev=statistics.stdev(educationList)
lunch_stdev=statistics.stdev(lunchList)
test_stdev=statistics.stdev(testList)
math_stdev=statistics.stdev(mathList)
reading_stdev=statistics.stdev(readingList)
writing_stdev=statistics.stdev(writingList)

gender_firstSd_start,gender_firstSd_end=gender_mean-gender_stdev,gender_mean+gender_stdev
gender_secondSd_start,gender_secondSd_end=gender_mean-(2*gender_stdev),gender_mean+(2*gender_stdev)
gender_thirdSd_start,gender_thirdSd_end=gender_mean-(3*gender_stdev),gender_mean+(3*gender_stdev)

race_firstSd_start,race_firstSd_end=race_mean-race_stdev,race_mean+race_stdev
race_secondSd_start,race_secondSd_end=race_mean-(2*race_stdev),race_mean+(2*race_stdev)
race_thirdSd_start,race_thirdSd_end=race_mean-(3*race_stdev),race_mean+(3*race_stdev)

education_firstSd_start,education_firstSd_end=education_mean-education_stdev,education_mean+race_stdev
education_secondSd_start,education_secondSd_end=education_mean-(2*education_stdev),education_mean+(2*education_stdev)
education_thirdSd_start,education_thirdSd_end=education_mean-(3*education_stdev),education_mean+(3*education_stdev)

lunch_firstSd_start,lunch_firstSd_end=lunch_mean-lunch_stdev,lunch_mean+lunch_stdev
lunch_secondSd_start,lunch_secondSd_end=lunch_mean-(2*lunch_stdev),lunch_mean+(2*lunch_stdev)
lunch_thirdSd_start,lunch_thirdSd_end=lunch_mean-(3*lunch_stdev),lunch_mean+(3*lunch_stdev)

test_firstSd_start,test_firstSd_end=test_mean-test_stdev,test_mean+test_stdev
test_secondSd_start,test_secondSd_end=test_mean-(2*test_stdev),test_mean+(2*test_stdev)
test_thirdSd_start,test_thirdSd_end=test_mean-(3*test_stdev),test_mean+(3*test_stdev)

math_firstSd_start,math_firstSd_end=math_mean-math_stdev,math_mean+math_stdev
math_secondSd_start,math_secondSd_end=math_mean-(2*math_stdev),math_mean+(2*math_stdev)
math_thirdSd_start,math_thirdSd_end=math_mean-(3*math_stdev),math_mean+(3*math_stdev)

reading_firstSd_start,reading_firstSd_end=reading_mean-reading_stdev,reading_mean+reading_stdev
reading_secondSd_start,reading_secondSd_end=reading_mean-(2*reading_stdev),reading_mean+(2*reading_stdev)
reading_thirdSd_start,reading_thirdSd_end=reading_mean-(3*reading_stdev),reading_mean+(3*reading_stdev)

writing_firstSd_start,writing_firstSd_end=writing_mean-writing_stdev,writing_mean+writing_stdev
writing_secondSd_start,writing_secondSd_end=writing_mean-(2*writing_stdev),writing_mean+(2*writing_stdev)
writing_thirdSd_start,writing_thirdSd_end=writing_mean-(3*writing_stdev),writing_mean+(3*writing_stdev)

genderData_firstSd=[result for result in genderList if result > gender_firstSd_start and result < gender_firstSd_end]
genderData_secondSd=[result for result in genderList if result > gender_secondSd_start and result < gender_secondSd_end]
genderData_thirdSd=[result for result in genderList if result > gender_thirdSd_start and result < gender_thirdSd_end]

raceData_firstSd=[result for result in raceList if result > race_firstSd_start and result < race_firstSd_end]
raceData_secondSd=[result for result in raceList if result > race_secondSd_start and result < race_secondSd_end]
raceData_thirdSd=[result for result in raceList if result > race_thirdSd_start and result < race_thirdSd_end]

educationData_firstSd=[result for result in educationList if result > education_firstSd_start and result < education_firstSd_end]
educationData_secondSd=[result for result in educationList if result > education_secondSd_start and result < education_secondSd_end]
educationData_thirdSd=[result for result in educationList if result > education_thirdSd_start and result < education_thirdSd_end]

lunchData_firstSd=[result for result in lunchList if result > lunch_firstSd_start and result < lunch_firstSd_end]
lunchData_secondSd=[result for result in lunchList if result > lunch_secondSd_start and result < lunch_secondSd_end]
lunchData_thirdSd=[result for result in lunchList if result > lunch_thirdSd_start and result < lunch_thirdSd_end]

testData_firstSd=[result for result in testList if result > test_firstSd_start and result < test_firstSd_end]
testData_secondSd=[result for result in testList if result > test_secondSd_start and result < test_secondSd_end]
testData_thirdSd=[result for result in testList if result > test_thirdSd_start and result < test_thirdSd_end]

mathData_firstSd=[result for result in mathList if result > math_firstSd_start and result < math_firstSd_end]
mathData_secondSd=[result for result in mathList if result > math_secondSd_start and result < math_secondSd_end]
mathData_thirdSd=[result for result in mathList if result > math_thirdSd_start and result < math_thirdSd_end]

readingData_firstSd=[result for result in readingList if result > reading_firstSd_start and result < reading_firstSd_end]
readingData_secondSd=[result for result in readingList if result > reading_secondSd_start and result < reading_secondSd_end]
readingData_thirdSd=[result for result in readingList if result > reading_thirdSd_start and result < reading_thirdSd_end]

writingData_firstSd=[result for result in writingList if result > writing_firstSd_start and result < writing_firstSd_end]
writingData_secondSd=[result for result in writingList if result > writing_secondSd_start and result < writing_secondSd_end]
writingData_thirdSd=[result for result in writingList if result > writing_thirdSd_start and result < writing_thirdSd_end]

print('{} % of data for gender lies within firstStdev'.format(len(genderData_firstSd)*100/len(genderList)))
print('{} % of data for gender lies within secondStdev'.format(len(genderData_secondSd)*100/len(genderList)))
print('{} % of data for gender lies within thirdStdev'.format(len(genderData_thirdSd)*100/len(genderList)))

print('{} % of data for race lies within firstStdev'.format(len(raceData_firstSd)*100/len(raceList)))
print('{} % of data for race lies within secondStdev'.format(len(raceData_secondSd)*100/len(raceList)))
print('{} % of data for race lies within thirdStdev'.format(len(raceData_thirdSd)*100/len(raceList)))

print('{} % of data for education lies within firstStdev'.format(len(educationData_firstSd)*100/len(educationList)))
print('{} % of data for education lies within secondStdev'.format(len(educationData_secondSd)*100/len(educationList)))
print('{} % of data for education lies within thirdStdev'.format(len(educationData_thirdSd)*100/len(educationList)))

print('{} % of data for lunch lies within firstStdev'.format(len(lunchData_firstSd)*100/len(lunchList)))
print('{} % of data for lunch lies within secondStdev'.format(len(lunchData_secondSd)*100/len(lunchList)))
print('{} % of data for lunch lies within thirdStdev'.format(len(lunchData_thirdSd)*100/len(lunchList)))

print('{} % of data for test lies within firstStdev'.format(len(testData_firstSd)*100/len(testList)))
print('{} % of data for test lies within secondStdev'.format(len(testData_secondSd)*100/len(testList)))
print('{} % of data for test lies within thirdStdev'.format(len(testData_thirdSd)*100/len(testList)))

print('{} % of data for math lies within firstStdev'.format(len(mathData_firstSd)*100/len(mathList)))
print('{} % of data for math lies within secondStdev'.format(len(mathData_secondSd)*100/len(mathList)))
print('{} % of data for math lies within thirdStdev'.format(len(mathData_thirdSd)*100/len(mathList)))

print('{} % of data for reading lies within firstStdev'.format(len(readingData_firstSd)*100/len(readingList)))
print('{} % of data for reading lies within secondStdev'.format(len(readingData_secondSd)*100/len(readingList)))
print('{} % of data for reading lies within thirdStdev'.format(len(readingData_thirdSd)*100/len(readingList)))

print('{} % of data for writing lies within firstStdev'.format(len(writingData_firstSd)*100/len(writingList)))
print('{} % of data for writing lies within secondStdev'.format(len(writingData_secondSd)*100/len(writingList)))
print('{} % of data for writing lies within thirdStdev'.format(len(writingData_thirdSd)*100/len(writingList)))