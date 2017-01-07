format long g
X=[train(:,2) train(:,3)];
X=cell2mat(X);
time=train(:,1);
time=cell2mat(time);
plot(X(:,1),X(:,2),'.') 
[IDX,C] = kmeans(X,39)
id=train(:,4);
id=char(id);
k=strmatch('80c48',id,'exact'); 
number=1;
matrix=ones(length(k),4);
for n=1:length(k)
    matrix(number,1)=time(k(n));
    matrix(number,2)=X(k(n),1);
    matrix(number,3)=X(k(n),2);
    matrix(number,4)=IDX(k(n));
    number=number+1;
end
bus_stop=unique(matrix(:,4),'stable');
number2=1;
for n=1:length(bus_stop)
    coord(number2,1)=C(bus_stop(n),1);
    coord(number2,2)=C(bus_stop(n),2);
    number2=number2+1;
end
final_coord=coord(2:38,1:2);

 