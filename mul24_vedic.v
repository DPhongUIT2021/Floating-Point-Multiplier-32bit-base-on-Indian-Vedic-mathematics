



module mul24_vedic(A, B, O);
		parameter msb = 23;
		parameter gnd_msk8 = 8'b0000_0000, gnd_msk7 = 7'b000_0000, gnd_msk6 = 6'b00_0000;
		input[msb:0] A, B;
		output[msb*2+1:0] O;
		
		wire[15:0] m0, m1, m2, m3, m4, m5, m6, m7, m8;
		wire[15:0] a0, a1, a2, a3, a4, a5, a8, a9;
		wire[7:0] a6;
		wire a7, a10;
		wire over0, over1, over2, over3, over4, over5, over6, over7, over8;
		wire[7:0] A2, A1, A0, B2, B1, B0;
		wire over01, over10;
		
		mul8_vedic mu0(.A(A0), .B(B0), .O(m0));
		mul8_vedic mu1(.A(A0), .B(B1), .O(m1));
		mul8_vedic mu2(.A(A1), .B(B0), .O(m2));
		mul8_vedic mu3(.A(A0), .B(B2), .O(m3));
		mul8_vedic mu4(.A(A1), .B(B1), .O(m4));
		mul8_vedic mu5(.A(A2), .B(B0), .O(m5));
		mul8_vedic mu6(.A(A1), .B(B2), .O(m6));
		mul8_vedic mu7(.A(A2), .B(B1), .O(m7));
		mul8_vedic mu8(.A(A2), .B(B2), .O(m8));

		adder16 adder0(.A(m2), .B(m1), .O(a0), .carry_out(over0));
		adder16 adder1(.A(a0), .B({gnd_msk8, m0[15:8]}), .O(a1), .carry_out(over1));
		adder16 adder2(.A(m5), .B(m4), .O(a2), .carry_out(over2));
		adder16 adder3(.A(a2), .B(m3), .O(a3), .carry_out(over3));
		adder16 adder4(.A(a3), .B({gnd_msk7, over01, a1[15:8]}), .O(a4), .carry_out(over4));
		adder16 adder5(.A(m7), .B(m6), .O(a5), .carry_out(over5));
		full_adder adder7(.sum(a7), .c_out(over7), .a(over2), .b(over3), .c_in(over4));
		adder16 adder8(.A(a5), .B({gnd_msk6, over7, a7, a4[15:8]}), .O(a8), .carry_out(over8));
		adder16 adder9(.A(m8), .B({gnd_msk6, over10, a10, a8[15:8]}), .O(a9), .carry_out());
		full_adder adder10(.sum(a10), .c_out(over10), .a(over5), .b(over8), .c_in(0));
		
		assign over01 = (over0 | over1);
		assign A2 = A[23:16];
		assign A1 = A[15:8];
		assign A0 = A[7:0];
		assign B2 = B[23:16];
		assign B1 = B[15:8];
		assign B0 = B[7:0];
		assign O[msb*2+1:0] = {a9[15:0], a8[7:0], a4[7:0], a1[7:0], m0[7:0]};
		
endmodule






















