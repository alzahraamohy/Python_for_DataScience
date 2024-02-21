import statistics as st      #first line for all these examples

1) st.mean()     >>> calculate the average
#example
b=[1,2,3,4,5,6]    #can be a list or tuple or set NOT dictionary
a=st.mean(b)
print(a)


2)st.harmonic_mean()   >>> divide n / ( (1/n1) + (1/n2) + ....) 
#ex
a = st.harmonic_mean( [7,2,3,6,9,33,2.5])
print(a)

3) st.median()      >>> the middle number in an ordered set
                        but if the number of elements are even, we divide the sum of the 2 middle numbers by 2
#ex
a = st.median( [3,6,9,4,5,3.2,9,7])
print(a)

4) st.median_low()     >>> in the case of even number of elements it takes the lower number
#ex
a = st.median_low( [3,6,9,4,5,3.2,9,7,9])
print(a)

5) st.median_high()      >>> takes the higher
#ex
a = st.median_high( [3,6,9,4,5,3.2,9,7,9])
print(a)

6) st.mode()          >>> the most repeated number
#ex
a = mode( [2,3,5,4,2,3,6,9,8,5,2,2,3,4,6])
print(a)

7) st.stdev()          >>> Standard deviation is a measure of the amount of variation or dispersion in a set of values.
                          In other words, it quantifies the amount of variability or spread in a dataset.
  # بيقيس مقدار التنوع يعني لو عندنا 3 فصول واحد متفوقين وواحد فاشلين وواحد فيه متفوقين وفاشلين , بالتالي مقدار التنوع في الفصل التالت اكبر
#ex
a = st.stdev([3.2,6.9,8.1,-9.3,66])
print(a)

8)st.variance()        >>> Measures the amount of variation
#بيقيس مقدار الاختلاف
#ex
a = st.variance([3.2,6.9,8.1,-9.3,66])
print(a)













