from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Portfólio</title>
        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');
            body { font-family: 'Poppins', sans-serif; margin: 0; padding: 0; text-align: center; background-color: #000; color: #fff; overflow-y: auto; }
            nav { position: fixed; top: 0; width: 100%; background: #222; padding: 15px; text-align: center; box-shadow: 0px 4px 10px rgba(255, 0, 0, 0.5); z-index: 1000; }
            nav a { display: inline-block; background: #8B0000; color: #fff; padding: 10px 25px; margin: 5px; text-decoration: none; font-weight: bold; border-radius: 5px; transition: background 0.3s, color 0.3s, transform 0.3s; }
            nav a:hover { background: #fff; color: #8B0000; transform: scale(1.1); }
            header { background: linear-gradient(90deg, #8B0000, #000); color: #fff; padding: 100px; font-size: 36px; font-weight: bold; text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.7); margin-top: 100px; }
            section { margin: 40px 20px 20px; padding: 20px; background: #111; border-radius: 15px; box-shadow: 5px 5px 15px rgba(255, 0, 0, 0.5); transition: transform 0.3s, box-shadow 0.3s; }
            section:hover { transform: scale(1.05); box-shadow: 10px 10px 20px rgba(255, 0, 0, 0.7); }
            a { color: #8B0000; text-decoration: none; font-weight: bold; transition: color 0.3s; }
            a:hover { color: #fff; text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8); }
            #particles-js { position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1; }
        </style>
    </head>
    <body>
        <div id="particles-js"></div>
        <nav>
            <a href="#sobre">Sobre</a>
            <a href="#projetos">Projetos</a>
            <a href="#curriculo">Currículo</a>
            <a href="#contato">Contato</a>
        </nav>
        <header>Meu Portfólio</header>
        <section id="sobre">
            <h2>Sobre Mim</h2>
            <p>Olá! Meu nome é Salatiel Alves e sou um desenvolvedor apaixonado por tecnologia focado em soluções inovadoras e de alta performance.</p>
        </section>
        <section id="projetos">
            <h2>Projetos</h2>
            <p>Confira meus projetos no <a href="https://github.com/Salatiel-T-Alves" target="_blank">GitHub</a>.</p>
        </section>
        <section id="curriculo">
            <h2>Currículo</h2>
            <p><strong>Formação:</strong> Análise e Desenvolvimento De Sistemas ( ADS )</p>
            <p><strong>Experiência:</strong> Estudante de ADS apaixonado por tecnologia, focado em solução.</p>
            <p><strong>Habilidades:</strong> Python, JavaScript, Flask, React, Banco de Dados</p>
            <p><a href="https://www.canva.com/design/DAGgB40YAMI/25TVReHYW3CXjNmmI8KA5A/view?utm_content=DAGgB40YAMI&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hca761af3bf" target="_blank" style="color: #8B0000; text-decoration: underline;">Acessar Currículo</a></p>
        </section>
        <section id="contato">
            <h2>Contato</h2>
            <p>Entre em contato pelo e-mail: <strong>salatiel.dev.javascript@gmail.com</strong></p>
        </section>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                particlesJS("particles-js", {
                    particles: {
                        number: { value: 100 },
                        size: { value: 3 },
                        move: { speed: 2 },
                        color: { value: "#8B0000" },
                        line_linked: { enable: true, color: "#fff" }
                    }
                });

                document.querySelectorAll('nav a').forEach(anchor => {
                    anchor.addEventListener('click', function(e) {
                        e.preventDefault();
                        const targetId = this.getAttribute('href').substring(1);
                        document.getElementById(targetId).scrollIntoView({
                            behavior: 'smooth'
                        });
                    });
                });
            });
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
