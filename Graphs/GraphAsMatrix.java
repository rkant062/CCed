import java.util.Scanner;

public class GraphAsMatrix {
	private static int vertices;
	private static int matrix[][];

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		vertices = sc.nextInt();
		matrix = new int[vertices][vertices];
		GraphAsMatrix gam = new GraphAsMatrix();
		gam.initializeMatrix(matrix);
		gam.addEdge(0, 1);gam.addEdge(1, 2);gam.addEdge(2, 5);gam.addEdge(5, 6);gam.addEdge(0,3);gam.addEdge(3, 4);gam.addEdge(4, 5);
		gam.printGraph(matrix);
		

	}

	public void initializeMatrix(int matrix[][]) {
		for (int i = 0; i < vertices; i++) {
			for (int j = 0; j < vertices; j++) {
				matrix[i][j] = 0;
			}
		}
	}

	public void printGraph(int matrix[][]) {
		for (int i = 0; i < vertices; i++) {
			for (int j = 0; j < vertices; j++) {
				System.out.print(matrix[i][j] + " ");
			}
			System.out.println();
		}
	}

	public void addEdge(int a, int b) {
		matrix[a][b] = 1;
		matrix[b][a] = 1;
	}
}
