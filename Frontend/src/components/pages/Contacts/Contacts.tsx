import "./contacts.scss"
import Logo from "../../utils/logo/Logo"
import photo1 from "../../assets/images/contacts/photo1.png"
import diagonal_arrow from "../../assets/icons/diagonal_arrow.svg"
import React from "react";

export const Contacts = () => {
    return (
        <section className="contacts-section">
            <Logo title="контакты" />
            <div className="container">
                <div className="row justify-content-center m-5 text-white contacts">
                    <div className="row contact h-100">
                        <div className="col-4 h-100 d-flex align-items-center">
                            <img src={photo1} className="img-fluid rounded-start" alt="..."/>
                        </div>
                        <div className="col-8 h-100 d-flex align-items-center">
                            <div>
                                <h5 className="contact-title">Бизиков Валерий</h5>
                                <p>Руководитель ЦМР</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="row row-cols-md-3 links m-5 text-center">
                    <div className="col-md mb-2">
                        <p>Телефон: <a className="text-light" href="tel:+78005553535">8(800)555-35-35</a></p>
                        <p>Email: <a className="text-light" href="mailto:cmr@bmstu.ru">cmr@bmstu.ru</a></p>
                    </div>
                    <div className="col-md mb-2">
                        <div>
                            <span>Адрес: </span>
                            <span className="text-light">105005, г. Москва, 2-ая Бауманская, д.5, стр.1</span>
                        </div>
                        <div>
                            <a className="text-light" href="">Схема проезда</a>
                            <img src={diagonal_arrow} className="diagonal-arrow" alt="..."/>
                        </div>
                    </div>
                    <div className="col-md mb-2">
                        <p className="text-white opacity-75">Соцсети:</p>
                        <div>
                            <a className="text-light" href="https://vk.com/robotics_bmstu">ВКонтакте</a>
                            <img src={diagonal_arrow} className="diagonal-arrow" alt="..."/>
                        </div>
                        <div>
                            <a className="text-light" href="https://t.me/robotics_bmstu">Телеграм</a>
                            <img src={diagonal_arrow} className="diagonal-arrow" alt="..."/>
                        </div>
                    </div>
                </div>
            </div>
            <footer>
                <p className="footer-text text-black">Developed @ 2023 by ITS tech</p>
            </footer>
        </section>
    )
}