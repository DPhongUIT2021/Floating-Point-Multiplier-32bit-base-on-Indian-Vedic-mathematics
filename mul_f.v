


module mul_f(A, B, O);
			parameter msb = 31;
			parameter[7:0] exp_bias = ~127;
			input[msb:0] A, B;
			output[msb:0] O;
			
			
			wire signA, signB, signO;
			wire[7:0] expA, expB, expO;
			wire[22:0] manA, manB, manO;
			wire[45:0] mul, out_shift;
			wire[47:0] out_mul24;
			wire[8:0] add0, sub0;
			wire sign_mul, over_flag, over_sub;
			//wire[8:0] exp_bias;
			
			//module mul24_vedic(A, B, O);
			mul24_vedic m0(.A({1'b1, manA}), .B({1'b1, manB}), .O(out_mul24));
			//adder9(A, B, carry_in, O, carry_out);
			adder9 adder0(.A({1'b0, expA}), .B({1'b0, expB}), .carry_in(sign_mul), .O(add0), .carry_out());
			adder9 suber0(.A(add0), .B(exp_bias), .carry_in(1), .O(sub0), .carry_out(over_sub));
			
			
			assign signA = A[msb];
			assign signB = B[msb];
			assign signO = (signA ^ signB);
			assign over_flag = (sub0[8] | over_sub);
			assign sign_mul = mul[45];
			assign expA = A[30:23];
			assign expB = B[30:23];
			assign expO = sub0[7:0];
			assign manA = A[22:0];
			assign manB = B[22:0];
			assign manO[22:0] = out_shift[43:21];
			assign mul[45:0] = out_mul24[47:2];
			assign out_shift[45:0] = sign_mul ? {1'b0, mul[45:1]} : mul[45:0];
			//assign exp_bias[8:0] = ~127;
			assign O[msb:0] = {signO, expO[7:0], manO[22:0]};
endmodule






























































