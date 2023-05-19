
`timescale 1ps/1ps
module tb_mul();
			parameter msb = 15, T = 4;
			
			reg [11:0] J;
			reg[15:0] sin;
			
			wire[31:0] O;
			wire[11:0] J_sin;
			wire[11:0] J_exten_sign;
			
			initial begin
				J = 12'hC74;
				sin = 16'h43CF;
			end
		
			always #(T) begin
					//A = A + k;
					//B = B + k;
			end
			//module mul2_vedic(a, b, o);
			//mul4_vedic md_mul(.A(A), .B(B), .O(O));
			mul16_vedic md_mul(.A({4'b1111, J}), .B(sin), .O(O));
			//mul16_vedic md_mul(.A(A), .B(B), .O(O));
			//mul24_vedic md_mul(.A(A), .B(B), .O(O));
			assign J_sin = O[26:15];
			assign J_exten_sign = {J[11], J_sin[10:0]};

endmodule

