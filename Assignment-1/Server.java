 import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

/**
 * Sebuah TCP server di port 9090.
 * fungsinya ketika client terkoneksi, server akan mengirimkan Tanggal sekarang
 * dan menutup koneksi
 */

public class Server {
        public static void main(String[] args) throws IOException {
        ServerSocket listener = new ServerSocket(8897);
        try {
            while (true) {
                Socket socket = listener.accept(); //server akan me-listen koneksi ke port 9090
                try {
                    PrintWriter out =
                        new PrintWriter(socket.getOutputStream(), true);
                    out.println("a");
                } finally {
                    socket.close();
                }
            }
        }
        finally {
            listener.close();
        }
    }
}
