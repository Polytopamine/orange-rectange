
%Newton Raphson Method
disp(" ---- Newton Raphson method ----")
syms x

% ---- variables:


%f = x^3-4*x^2-x+2;
%f = cos(x/2)-x/2;
%f  = x^2-2; % to find the value of sqrt(2)
%f=x-2+log(x); %use log for ln
%f = (0.001*x^4+0.02*x^2+0.1*x)*17*10^6-100;
f = (0.03*x^4+0.2*x^2+0.01*x)*21*10^8-1500;
precision = 9;
initial_guess = 0.5;


% ---------


f_diff = diff(f);
disp("original function: "+ string(f))
disp('diff f: '+ string(f_diff))
disp('inital guess: ' + string(initial_guess))



loop_counter = 0;
current_x = initial_guess;
delta_f=1;

while abs(delta_f) > 10^-precision
    
    f_x = round(subs(f, x, current_x), precision);
    f_diff_x = round(subs(f_diff, x, current_x), precision);
    delta_f = round(-f_x/f_diff_x, precision);

    disp(newline+"loop_counter: "+ string(loop_counter))
    disp("current_x: "+ string((vpa(current_x))))
    disp("f(x) = "+ string(vpa(f_x)))
    disp("f'(x) = "+ string(vpa(f_diff_x)))
    disp("delta_f = "+ string(vpa(delta_f)))

    current_x = round(current_x + delta_f, precision);
    loop_counter = loop_counter + 1;

end

disp(' ')
disp('starting from:')
disp("original function: "+ string(f))
disp('inital guess: ' + string(initial_guess))
disp('answer: ' + string(current_x))
