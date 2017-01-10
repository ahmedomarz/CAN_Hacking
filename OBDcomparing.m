%%opening the file and taking data into myArray
fid = fopen('output1.txt');
tline = fgetl(fid);
FirstOutput={};
while ischar(tline)
    FirstOutput = [FirstOutput; tline];
    tline = fgetl(fid);
end
fclose(fid);

fid = fopen('output2.txt');
tline = fgetl(fid);
SecondOutput={};
while ischar(tline)
    SecondOutput = [SecondOutput; tline];
    tline = fgetl(fid);
end
fclose(fid);


Acommon = intersect(FirstOutput,SecondOutput);
SecondOutput = setxor(SecondOutput,Acommon);


%%outputing the final result in an output file
filename = 'outputFinal.txt';
dlmwrite(filename, 1);
xlswrite(filename, SecondOutput);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%%opening the file and taking data into myArray
fid = fopen('obd.txt');
tline = fgetl(fid);
Output={};
while ischar(tline)
    Output = [Output; tline];
    tline = fgetl(fid);
end
fclose(fid);

lastOut = [];

for i=1:size(SecondOutput)
    num=0;
    for j = 1: size(Output)
        if strcmp (Output(j,:),SecondOutput(i))
            num=num+1;
        end
    end
    
    if num> 5 && num<100
        lastOut = [lastOut [SecondOutput(i) num2str(num)]];
    end
    
end


filename = 'lastOut.txt';
dlmwrite(filename, 1);
xlswrite(filename, lastOut');