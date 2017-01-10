%%opening the file and taking data into myArray
fid = fopen('obd.txt');
tline = fgetl(fid);
myArray={};
while ischar(tline)
    myArray = [myArray; tline];
    tline = fgetl(fid);
end
fclose(fid);

%%sorting and removing duplicates
myUniqueArray=unique(myArray);

%%counting number of repeated elements
%repeated=histc(sparce(myArray),myUniqueArray);

%%adding the msg and its repeating number in the same array
%newArray=horzcat(myUniqueArray,repeated);





%%removing substrings from full strings due to sending error
iterations=size(myUniqueArray);
k=1;
for i=1:iterations-1
    first=char(myUniqueArray(k));
    second=char(myUniqueArray(k+1));
    flag=0;
    if findstr(first,second)
        myUniqueArray(k)=[];
    else
        k=k+1;
    end
    
    iterations=size(myUniqueArray);
end


%%outputing the final result in an output file
filename = 'output2.txt';
dlmwrite(filename, 1);
xlswrite(filename, myUniqueArray);