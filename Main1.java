package hamburgerDistribute;
import java.util.Scanner;
import java.util.Arrays;
public class Main1 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		// table 책상의 길이
		// r 햄버거를 집을 수 있는 거리
		// HP 햄버거와 사람의 정보가 담겨있는 스트링
		// arr 햄버거와 사람의 정보가 담겨있는 배열
		// 햄버거를 먹은 사람의 명수
		int table = in.nextInt();
		int r = in.nextInt();
		String HP = in.next();
		int count = 0;
		
		// HP 를 arr배열에 변환하여 저장
		char[] arr = HP.toCharArray();
		
		
		// j = 햄버거를 찾는 커서
		// i = 사람을 찾는 커서
		int j = 0;
		for(int i = 0; i<table; i++) {
			// 사람을 찾았을 때
			if(arr[i] == 'P') {
				// 사람이 있는 곳에서 햄버거를 집을 수 있는 좌표가 0보다 낮을경오 0으로 설정
				if(i-r<0) {
					j = 0;
				}else{
					// 아닐경우 가장 왼쪽부터 탐색
					j = i-r;
				}
				// 왼쪽부터 오른쪽으로 탐색
				for(;j <= i+r ; j++) {
					// 햄버거를 찾았을 경우 0으로 바꾸고 햄버거 먹은 사람의 수를 올려줌
					if( j + r >= table-1) {
						j = table-1;
					}
					System.out.println("J = " + j);
					if(arr[j]=='H' ) {
						arr[j] = '0';
						count++;
						break;
					}
				}
				
			}
		}

		
		
		System.out.println(table + " " + r + " " + Arrays.toString(arr));
		
		System.out.println(count);
		
		
	}
}
