import React from 'react';
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Menu from "./components/utils/menu/Menu";
import {News} from "./components/pages/News/News";
import {Events} from "./components/pages/Events/Events";
import {Event} from "./components/pages/Event/Event";
import {Achievements} from "./components/pages/Achievements/Achievements";
import {Partners} from "./components/pages/Partners/Partners";
import {Contacts} from "./components/pages/Contacts/Contacts";
import {Home} from "./components/pages/Home/Home";
import {Hardathon} from "./components/pages/Hardathon/Hardathon";
import {PartnersHardathon} from "./components/pages/Hardathon/Partners/PartnersHard";
import {PartnersH} from "./components/pages/Hardathon/ProjectDetails/ProjectDetails";
import {Proj} from "./components/pages/Hardathon/Projects/Projects";


function App() {
    return (
    <Router>
        <Menu />
        <main>
            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/news" element={<News/>} />
                <Route path="/events" element={<Events/>} />
                <Route path="/event/:id" element={<Event/>} />
                <Route path="/achievements" element={<Achievements/>} />
                <Route path="/partners" element={<Partners/>} />
                <Route path="/contacts" element={<Contacts/>} />
                <Route path="/hardathon" element={<Hardathon/>} />
                <Route path="/hardathon/Partners" element={<PartnersHardathon/>} />
                <Route path="/hardathon/ProjectDetails" element={<PartnersH/>} />
                <Route path="/hardathon/Projects" element={<Proj/>} />
            </Routes>
        </main>
    </Router>
  );
}

export default App;
