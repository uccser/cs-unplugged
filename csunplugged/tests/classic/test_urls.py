from tests.BaseTestWithDB import BaseTestWithDB


class RedirectClassicUnpluggedURLsTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_activities(self):
        response = self.client.get("/activities")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/activities",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_activities_under_development(self):
        response = self.client.get("/activities-under-development")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/activities/community-activities/",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_artificial_intelligence(self):
        response = self.client.get("/artificial-intelligence")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/artificial-intelligence",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_binary_numbers(self):
        response = self.client.get("/binary-numbers")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/binary-numbers",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_books(self):
        response = self.client.get("/books")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/books",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_changelog(self):
        response = self.client.get("/changelog")
        self.assertRedirects(
            response,
            "https://cs-unplugged.readthedocs.io/changelog.html",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_class_simulation_computer_unfinished(self):
        response = self.client.get("/class-simulation-computer-unfinished")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/class-simulation-computer-unfinished",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_community(self):
        response = self.client.get("/community")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/community",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_community_activties(self):
        response = self.client.get("/community-activties")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/community-activties",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_contact_us(self):
        response = self.client.get("/contact-us", follow=True)
        self.assertRedirects(response, "/en/contact/", status_code=301)

    def test_contribute(self):
        response = self.client.get("/contribute")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/contribute",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_cryptographic_protocols(self):
        response = self.client.get("/cryptographic-protocols")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/cryptographic-protocols",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_curriculum_links(self):
        response = self.client.get("/curriculum-links")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/curriculum-links",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_databases(self):
        response = self.client.get("/databases")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/databases",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_divideandconquer(self):
        response = self.client.get("/divideandconquer")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/divideandconquer",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_dominating_sets(self):
        response = self.client.get("/dominating-sets")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/dominating-sets",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_error_detection(self):
        response = self.client.get("/error-detection")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/error-detection",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_events(self):
        response = self.client.get("/events")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/events",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_finite_state_automata(self):
        response = self.client.get("/finite-state-automata")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/finite-state-automata",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_graph_colouring(self):
        response = self.client.get("/graph-colouring")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/graph-colouring",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_harold_the_robot_2(self):
        response = self.client.get("/harold-the-robot-2")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/harold-the-robot-2",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_human_interface_design(self):
        response = self.client.get("/human-interface-design")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/human-interface-design",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_image_representation(self):
        response = self.client.get("/image-representation")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/image-representation",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_information_hiding(self):
        response = self.client.get("/information-hiding")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/information-hiding",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_information_theory(self):
        response = self.client.get("/information-theory")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/information-theory",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_line_drawing(self):
        response = self.client.get("/line-drawing")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/line-drawing",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_minimal_spanning_trees(self):
        response = self.client.get("/minimal-spanning-trees")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/minimal-spanning-trees",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_modems(self):
        response = self.client.get("/modem/")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/activities/community-activities/modems-unplugged/",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_modems_unplugged_2(self):
        response = self.client.get("/modems-unplugged-2")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/activities/community-activities/modems-unplugged/",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_network_protocols(self):
        response = self.client.get("/network-protocols")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/network-protocols",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_phylogenetics(self):
        response = self.client.get("/phylogenetics")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/phylogenetics",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_programming_languages(self):
        response = self.client.get("/programming-languages")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/programming-languages",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_projects(self):
        response = self.client.get("/projects")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/projects",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_promotional(self):
        response = self.client.get("/promotional")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/promotional",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_public_key_encryption(self):
        response = self.client.get("/public-key-encryption")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/public-key-encryption",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_research(self):
        response = self.client.get("/research")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/research",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_routing_and_deadlock(self):
        response = self.client.get("/routing-and-deadlock")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/routing-and-deadlock",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_scout_patrol_encryption(self):
        response = self.client.get("/scout-patrol-encryption")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/scout-patrol-encryption",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_searching_algorithms(self):
        response = self.client.get("/searching-algorithms")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/searching-algorithms",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_sneak_peek(self):
        response = self.client.get("/sneak-peek", follow=True)
        self.assertRedirects(response, "/en/", status_code=301)

    def test_sorting_algorithms(self):
        response = self.client.get("/sorting-algorithms")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/sorting-algorithms",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_sorting_networks(self):
        response = self.client.get("/sorting-networks")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/sorting-networks",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_steiner_trees(self):
        response = self.client.get("/steiner-trees")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/steiner-trees",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_teachers(self):
        response = self.client.get("/teachers")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/teachers",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_text_compression(self):
        response = self.client.get("/text-compression")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/text-compression",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_the_turing_test(self):
        response = self.client.get("/the-turing-test")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/the-turing-test",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_translations(self):
        response = self.client.get("/translations")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/translations",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_videos(self):
        response = self.client.get("/videos")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/videos",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_wp_content(self):
        response = self.client.get("/wp-content/")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/wp-content/",
            status_code=301,
            fetch_redirect_response=False
        )

    def test_wp_content_file(self):
        response = self.client.get("/wp-content/uploads/2015/03/CSUnplugged_OS_2015_v3.1.pdf")
        self.assertRedirects(
            response,
            "https://classic.csunplugged.org/wp-content/uploads/2015/03/CSUnplugged_OS_2015_v3.1.pdf",
            status_code=301,
            fetch_redirect_response=False
        )
